const express = require('express');
const app = express();
const bodyParser = require('body-parser')
const cookieParser = require('cookie-parser');
const TypingPractice = require('./TypingPractice')
const fileReader = require('fs')

app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

app.set('view engine', 'ejs');

const get_random_words = function(words, numberOfWords) {
    let words_str = ''
    for (let i = 0; i < numberOfWords; i++) {

        let item = words[Math.floor(Math.random()*words.length)];
        words_str = words_str + ' ' + item
    }
    return words_str
    
}


let wordsObj;

app.get('/', (req, res) => {
    
    let cookie = req.cookies.config;
    let config;
    if (cookie === undefined) {
        let randomNumber=Math.random().toString();
        randomNumber=randomNumber.substring(2,randomNumber.length);
        res.cookie('config', `{${randomNumber}},35,easy`);
        config = [35, 'easy'];
        console.log('There are no cookies')
    }else {
        const cookieParsed = cookie.split(',')
        config = [parseInt(cookieParsed[1]), cookieParsed[2]]
    }
    const difficulty = config[1]
    const nOfWords = config[0]
    let fileName;
    if (difficulty === 'easy') {
        fileName = './easy_difficulty.txt'
    }else {
        fileName = './words.txt'
    }
    console.log(fileName)
    const words_file = fileReader.readFileSync(fileName);
    // gets words from words.txt file and makes an array of those words
    const words = words_file.toString('utf8').split(',')
    const words_str = get_random_words(words, nOfWords)
    wordsObj = {
        text : words_str
    }
    res.render('index', {words: wordsObj})
})

app.post('/result', (req, res) => {
    /* This is how we get the input text
        and time. When the form is submitted, it submits the body's
        html and app is using body parser. see line 3 and 6
        the req object has a body attribute which has a wordsInput attribute as well as a timetaken attribute
        the last two attributes are from the name or id (not sure) of the html Elements
        the html input element which has the word's string has the id wordsInput and the element which has time
        has the id timeTaken
        see index.ejs
    */
    const inputText = req.body.wordsInput;
    const timeTaken = req.body.timeTaken;
    console.log(timeTaken);
    let resultArr = TypingPractice.TypingPractice(inputText, wordsObj.text.slice(1, wordsObj.text.length), parseInt(timeTaken)).getTypingData()
    let result = {
        wpm: resultArr[0],
        accuracy: resultArr[1],
        incorrectWords: resultArr[2],
        timeTaken: timeTaken,
    }
    console.log(result)
    res.render('result', { result: result });
})

app.get('/configure', (req, res) => {
    res.render('configure')
})

app.post('/addCookie', (req, res) => {
    const nOfChar = req.body.nOfChar;
    console.log(nOfChar, req.body.difficulty)
    let randomNumber=Math.random().toString();
    randomNumber=randomNumber.substring(2,randomNumber.length);
    res.cookie('config', `{${randomNumber}},${parseInt(nOfChar)},${req.body.difficulty}`);
    res.send('configuration finished <a href="/">back</a>')
})
app.listen(8000)