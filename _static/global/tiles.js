
const DECK = document.getElementById('deck');
const CARDS = document.getElementsByClassName('tile');
const MATCHED_COUPLE_DISPLAY = document.getElementById('matchedCoupleDisplay');

let openCardsHC = document.getElementsByClassName('open show');
let toBeReflippedHC = document.getElementsByClassName('toBeReflipped');
let matchCardsHC = document.getElementsByClassName('match');
let matchedCouplesNumber = 0;
let matchNumber = 1;
let idOrder = [];
let timer = null;


document.addEventListener('DOMContentLoaded', function() {
    liveSend({ 'status': "new_game" });
});


function liveRecv(data) {
    console.log("liveRecv data:", data);
    if (data['status'] === "new_game") {
        restartGame();
    }
    if (data['debug']) {
        console.log("Adjusting tile size for debug mode.");
        document.documentElement.style.setProperty('--tile-font-size', '12px');
    }
}

//Call function to shuffle cards and create HTML to display the cards
function newGame() {
    let cardsList = Array.prototype.slice.call(CARDS);
    let deckStr = "";
    cardsList = shuffle(cardsList);
    for (var i = 0; i < cardsList.length; i++) {
        DECK.appendChild(cardsList[i])

        // JSON Can't have a comma on the last entry, so add it here
        if (deckStr.length != 0) {
            deckStr += ','
        }
        idOrder.push(cardsList[i].id);
        deckStr += '\"' + i + '\":\"' + cardsList[i].classList[1] + '\"'
    }
}

//Calls newGame function, reset timer, reset open/shown/matched cards, reset move number and matched cards number.
function restartGame() {
    newGame();
    console.log(`Starting new game. Match number: ${matchNumber}, ${matchCardsHC.length} matched cards, ${openCardsHC.length} open cards.`);

    if (matchCardsHC.length > 0 || openCardsHC.length > 0) {
        resetCards();
    };
    if (matchedCouplesNumber !== 0) {
        matchedCouplesNumber = 0;
        MATCHED_COUPLE_DISPLAY.textContent = matchedCouplesNumber;
    }

    matchNumber++;
}

// Shuffle function from http://stackoverflow.com/a/2450976
function shuffle(array) {
    let currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}

// Flip cards, store open/shown cards images in an array, run check matching cards function, and prevent more 
// than 2 cards from being flipped.
function flipCard(evt) {
    // Disable click response if there is more then one flipped card
    if ($('.show').length > 1) {
        return true;
    }

    let flippedCard = evt.target;
    if (flippedCard.nodeName === 'LI') {
        if (!flippedCard.classList.contains('match') && !flippedCard.classList.contains('open')) {
            flippedCard.classList.add('open', 'show');
        }
    }
    let openCardsArray = Array.prototype.slice.call(openCardsHC);
    if (openCardsArray.length === 2) {
        checkIfMatching();
    }
    if (openCardsArray.length > 2) {
        flipOpenCards();
    }
}

// When 2 cards are open/shown, if their content match, assign class match, call function to unassign open/shown classes, 
// add +1 matching couple found, call function check if game is over. 
//
// If they don't match, assign a temporary class to identity which cards need to be closed in case more than 2 cards were 
// flipped, and call the function to close those 2 cards. 
//
// In any case, the move number is incremented by one
function checkIfMatching() {
    let openCardsArray = Array.prototype.slice.call(openCardsHC);
    if (openCardsArray[0].classList[1] === openCardsArray[1].classList[1]) {
        openCardsArray.forEach(function (card) {
            card.classList.add('match');
        });
        handleMatchedCards();
        incrementMatchedCouples();
        setTimeout(checkIfGameOver, 1200);
    } else {
        openCardsArray.forEach(function (card) {
            card.classList.add('toBeReflipped');
        });
        setTimeout(flipOpenCards, 1200);
    }
}

// Close the 2 cards confronted and any other open card, preventing there to be more than 1 open card besides the matched ones
function flipOpenCards() {
    let toBeReflipped = Array.prototype.slice.call(toBeReflippedHC);
    toBeReflipped.forEach(function (card) {
        card.classList.remove('open', 'show', 'toBeReflipped');
    });
    let openCardsArray = Array.prototype.slice.call(openCardsHC);
    if (openCardsArray.length > 1) {
        openCardsArray.forEach(function (card) {
            card.classList.remove('open', 'show');
        });
    }
}

//remove open/show class to the matched couple
function handleMatchedCards() {
    let matchCardsArray = Array.prototype.slice.call(matchCardsHC);
    matchCardsArray.forEach(function (card) {
        card.classList.remove('open', 'show');
    });
}

//remove open/show/match class to all matched cards.
function resetCards() {
    console.log("Resetting cards");
    let openCardsArray = Array.prototype.slice.call(openCardsHC);
    openCardsArray.forEach(function (card) {
        card.classList.remove('open', 'show');
    });
    let matchCardsArray = Array.prototype.slice.call(matchCardsHC);
    matchCardsArray.forEach(function (card) {
        card.classList.remove('match');
    });
}

//Increment matched couple number and display it
function incrementMatchedCouples() {
    matchedCouplesNumber++;
    MATCHED_COUPLE_DISPLAY.textContent = matchedCouplesNumber;
}

//Check if all the couples have been matched
function checkIfGameOver() {
    let matchCardsArray = Array.prototype.slice.call(matchCardsHC);
    console.log("Tiles: " + CARDS.length + ", Matched: " + matchCardsArray.length)
    if (matchCardsArray.length === CARDS.length) {
        liveSend({ 'status': 'success'});
    } else {
        return;
    }
}

//EVENT LISTENERS
DECK.addEventListener('click', flipCard);
