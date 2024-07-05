function isPortOpen(port, callback) {
    const net = require('net');
    const tester = net.createConnection({ port: port, host: '127.0.0.1' });

    const handleCleanup = () => {
        tester.removeAllListeners(); // Remove all listeners to prevent memory leaks
        tester.destroy();            // Ensure the socket is fully closed
    };

    tester.on('connect', () => {
        handleCleanup();
        callback(true);
    });

    tester.on('error', (err) => {
        handleCleanup();
        if (err.code === "ECONNREFUSED") {
            callback(false);
        } else {
            console.error('Unexpected error on checking port:', err);
            callback(false); // You might want to handle unknown errors differently
        }
    });

    tester.setTimeout(10000, () => { // Timeout after 10 seconds
        console.log(`Timeout: Port ${port} is not responding`);
        handleCleanup();
        callback(false);
    });
}

