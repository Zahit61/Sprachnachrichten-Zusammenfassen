const { fileURLToPath } = require('url');

// Include Nodejs' net module.
    Net = require('net');
//include fileSystem
    fileSystem = require('fs');
    path = require('path');

function sendFile(data){
    
    // The port number and hostname of the server.
    const port = 8080;
    const host = '127.0.0.1';
    const ADDR = (host,port);
    console.log("Bereich 1");
    // Create a new TCP client.
    const conn = new Net.Socket();
    // Send a connection request to the server.
    console.log("Bereich 2");
    conn.connect(8080, function () {
        // If there is no error, the server has accepted the request and created a new 
        // socket dedicated to us.
        console.log('TCP connection established with the server.');
        /*var filePath = path.join(__dirname, 'Lars2.ogg');
        var stat = fileSystem.statSync(filePath);*/

        /*response.writeHead(200, {
            'Content-Type': 'audio/ogg',
            'Content-Length': stat.size
        }); */

        // The client can now send data to the server by writing to its socket.
        conn.write();
    });

    // The client can also receive data from the server by reading from its socket.
    conn.on('data', function(chunk) {
        console.log(`Data received from the server: ${chunk.toString()}.`);
        
        // Request an end to the connection after the data has been received.
        conn.end();
    });

    conn.on('end', function() {
        console.log('Requested an end to the TCP connection');
    });
}

sendFile(); 