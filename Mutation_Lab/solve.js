const express = require('express');
const cookieParser = require('cookie-parser');
const session = require('cookie-session');
const app = express();

app.use(cookieParser());

app.use(session({name:'session',keys:["5921719c3037662e94250307ec5ed1db"],signed:true}  ));

app.get('/',(req,res) => {
        req.session.username="admin";
        res.send(`Hey there,take a look at the admin cookie`);
    }
)


app.listen(1234)
