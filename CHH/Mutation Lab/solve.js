const express = require('express')
const app = express()
const session = require('cookie-session')
app.use(session({
    name: 'session',
    keys: ['5921719c3037662e94250307ec5ed1db']
}))
app.get('/', (req, res) => {
    req.session.username = 'admin'
    res.send('hello')
})
app.listen(8081)