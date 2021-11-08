module.exports.TypingPractice = function(userWordsStr, wordsStr, timeTaken) {
    return {
        getTypingData: function() {
            const correctWordsAndIncorrectWords = this.getCorrectWords(wordsStr, userWordsStr);
            const correctWords = correctWordsAndIncorrectWords[0]
            const incorrectWords = correctWordsAndIncorrectWords[1]
            const totalCorrectCharacters = correctWordsAndIncorrectWords[2] + correctWords.length + incorrectWords.length - 1;
            const defaultNumberOfWords = totalCorrectCharacters / 5
            
            const wpm = (defaultNumberOfWords * 60) / timeTaken;
            const accuracy = totalCorrectCharacters / wordsStr.length * 100;
            return [Math.round(wpm, 1), Math.round(accuracy, 1), incorrectWords];
            
        },
        getCorrectWords: function(defaultWords, userWordsStr) {
            const defaultWordsList = defaultWords.split(' ')
            const userWordsList = userWordsStr.split(' ')
            let correctWordsList = []
            let incorrectWordsList = []
            let nOfCorrectCharacters = 0
            let nOfIncorrectCharacters = 0
            for (let i = 0; i < defaultWordsList.length; i++) {
                let defaultWord = defaultWordsList[i]
                let userWord = userWordsList[i]
                if (defaultWord == userWord) {
                    if (defaultWord != undefined && userWord != undefined) {
                        correctWordsList.push(userWord)
                        nOfCorrectCharacters = nOfCorrectCharacters + defaultWord.length
                    }
                    
                }else {
                    if (defaultWord != undefined && userWord != undefined) {
                        incorrectWordsList.push(userWord)
                        nOfIncorrectCharacters = nOfIncorrectCharacters + defaultWord.length
                    }
                    
                }
            }
            return [correctWordsList, incorrectWordsList, nOfCorrectCharacters, nOfIncorrectCharacters]
        }
    }
}

