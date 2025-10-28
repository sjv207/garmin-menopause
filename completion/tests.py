from otree.api import Bot
from .pages import (Finish, NonConsent, AttentionCheckFail)


class PlayerBot(Bot):
    def play_round(self):
        # Only yield the page that will be displayed based on player status
        if self.player.participant.vars.get('status') == "Non-Consent":
            yield NonConsent
        elif self.player.participant.vars.get('status') == "Atn-Check-Fail":
            yield AttentionCheckFail
        else:
            # Player is in "PLAYING" status
            yield Finish
        # yield Results
