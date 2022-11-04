const { json } = require('express')
const express = require('express')

const app = express()
app.use(express.json())
app.use(express.urlencoded())
app.post('/',(request, response)=>{
    const body = request.body
    response.send(200,(parseFloat(body["num1"]) + parseFloat(body["num2"])))
})

app.listen(3001,()=>{
    console.log("Server started successfully on port 3001");
})