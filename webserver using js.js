var http = require('http')
http.createServer(function(req,res){
    res.write("Welcome gosht")
    res.end()
}).listen(50051)