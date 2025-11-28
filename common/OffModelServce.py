import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ###########################################################################
# ####################### CLASSES ###########################################
# ###########################################################################


class TitToWorkPlayerScores(object):

    def __init__(self,
                 id: int,
                 player_id: str,
                 solo_score: int,
                 team_score: int,
                 team_p1_id: str,
                 team_p1_score: int,
                 team_p2_id: str,
                 team_p2_score: int,
                 team_p3_id: str,
                 team_p3_score: int,
                 comp_score: int,
                 comp_p1_id: str,
                 comp_p1_score: int,
                 comp_p2_id: str,
                 comp_p2_score: int,
                 comp_p3_id: str,
                 comp_p3_score: int

                 ) -> None:
        self.id = id
        self.player_id = player_id
        self.solo_score = solo_score
        self.team_score = team_score
        self.team_p1_id = team_p1_id
        self.team_p1_score = team_p1_score
        self.team_p2_id = team_p2_id
        self.team_p2_score = team_p2_score
        self.team_p3_id = team_p3_id
        self.team_p3_score = team_p3_score
        self.comp_score = comp_score
        self.comp_p1_id = comp_p1_id
        self.comp_p1_score = comp_p1_score
        self.comp_p2_id = comp_p2_id
        self.comp_p2_score = comp_p2_score
        self.comp_p3_id = comp_p3_id
        self.comp_p3_score = comp_p3_score
        self.created_time = int(time.time())

    def __repr__(self) -> str:
        return f'FitToWorkPlayerScores(id:{self.id}, player_id:{self.player_id}, solo_score:{self.solo_score}, ' \
            f'team_score:{self.team_score}, comp_score:{self.comp_score})'


# ###########################################################################
# ########################### The Service  ##################################
# ###########################################################################
class OffModelService(object):
    """ A service method for managing the off model entities

        Provides methods for adding and editing the off model entities
    """

    def __init__(self, connection_pool, name) -> None:
        # Connect to the database for the lifetime of this class
        self.connection = None
        self._create_db_connection(connection_pool, name)

    def __del__(self):
        # Close the database connection when the class is no longer in use
        # logger.info("Service destructor called")
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            # logger.info("Database connection closed")

    # ###########################################################################
    # ######################### PUBLIC METHODS ##################################
    # ###########################################################################

    # Create a player
    def persist_player(self, player: TitToWorkPlayerScores) -> TitToWorkPlayerScores:
        """ Create a new Player

        Args:
            player: A fully populated Player object

        Returns:
            The newly created Player object

        """
        ret_val = self._create_player(player)
        return ret_val

    def get_player(self, player_id: str) -> TitToWorkPlayerScores:
        query = "SELECT * FROM fittowork_player_scores WHERE player_id = %s"
        args = [id]

        row = self._execute_select(query, args)
        if row is not None:
            return self._build_player_from_db_row(row)
        else:
            raise Exception(f"Could not find Player for id: {player_id}")

    # #########################################################
    #   Private methods
    # #########################################################

    def _create_db_connection(self, connection_pool, name: str) -> None:
        if self.connection:
            self.connection.close()
            # logger.info("Database connection closed, going to re-open")

        try:
            self.connection = connection_pool.get_connection()
            # logger.info(f"Got a database connection for {name}")

        except Exception as err:
            logger.error(f"Could not get a database connection: {err}")

    def _create_player(self, player: TitToWorkPlayerScores) -> TitToWorkPlayerScores:
        query = "INSERT INTO fittowork_player_scores (player_id,solo_score,team_score,team_p1_id,team_p1_score,team_p2_id," \
                "team_p2_score,team_p3_id,team_p3_score,comp_score,comp_p1_id,comp_p1_score,comp_p2_id,comp_p2_score,comp_p3_id," \
                "comp_p3_score) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = [player.player_id, player.solo_score, player.team_score,
                player.team_p1_id, player.team_p1_score,
                player.team_p2_id, player.team_p2_score, player.team_p3_id, player.team_p3_score,
                player.comp_score, player.comp_p1_id, player.comp_p1_score, player.comp_p2_id, player.comp_p2_score, player.comp_p3_id,
                player.comp_p3_score]

        id = self._execute_insert_no_commit(query, args)
        # Commit this immediately
        self._execute_commit()
        player.id = id

        return player

    def _build_player_from_db_row(self, row) -> TitToWorkPlayerScores:
        player = TitToWorkPlayerScores(
            id=row[0],
            player_id=row[1],
            solo_score=row[2],
            team_score=row[3],
            team_p1_id=row[4],
            team_p1_score=row[5],
            team_p2_id=row[6],
            team_p2_score=row[7],
            team_p3_id=row[8],
            team_p3_score=row[9],
            comp_score=row[10],
            comp_p1_id=row[11],
            comp_p1_score=row[12],
            comp_p2_id=row[13],
            comp_p2_score=row[14],
            comp_p3_id=row[15],
            comp_p3_score=row[16]
        )
        return player

    # #########################################################
    #   Private generic methods
    # #########################################################

    def _execute_update_no_commit(self, query: str, args):
        cur = None

        try:
            if self.connection.is_connected():
                # logger.debug(f'Executing: {query}, args: {args}')
                cur = self.connection.cursor()
                cur.execute(query, args)
            else:
                logger.error("Not connected any more")

        except Exception as e:
            logger.error(f'Failed to execute UPDATE: {e}')
        finally:
            if cur:
                cur.close()

    def _execute_insert_no_commit(self, query: str, args):
        try:
            # logger.debug(f'Executing: {query}, args: {args}')
            cur = self.connection.cursor()
            cur.execute(query, args)
            id = cur.lastrowid
            return id

        except Exception as e:
            logger.error(f'Failed to INSERT INTO {e}')
        finally:
            if cur:
                cur.close()

    def _execute_select(self, query: str, args):
        cur = None

        try:
            if self.connection.is_connected():
                # logger.debug(f'Executing: {query}, args: {args}')
                cur = self.connection.cursor()
                cur.execute(query, args)
                row = cur.fetchone()
                return row
            else:
                logger.error("Not connected any more")

        except Exception as e:
            logger.error(f'Failed to execute SELECT: {e}')
        finally:
            if cur:
                cur.close()

    def _execute_select_many(self, query: str, args):
        cur = None

        try:
            if self.connection.is_connected():
                # logger.debug(f'Executing: {query}, args: {args}')
                cur = self.connection.cursor()
                cur.execute(query, args)
                rows = cur.fetchall()
                return rows
            else:
                logger.error("Not connected any more")

        except Exception as e:
            logger.error(f'Failed to execute SELECT: {e}')
        finally:
            if cur:
                cur.close()

    def _execute_commit(self) -> None:
        try:
            if self.connection.is_connected():
                # logger.debug('Commiting any changes')
                self.connection.commit()
            else:
                logger.error("Not connected any more")

        except Exception as e:
            logger.error(f'Failed to COMMIT: {e}')
