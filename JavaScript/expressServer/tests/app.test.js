const app = require('../app');
const request = require('http');

describe('GET /', () => {
  it('should respond with "Hello, world!"', done => {
    const req = request.request({
      hostname: 'localhost',
      port: 3000,
      path: '/',
      method: 'GET'
    }, res => {
      expect(res.statusCode).toBe(200);
      
      let data = '';
      res.on('data', chunk => {
        data += chunk;
      });

      res.on('end', () => {
        expect(data).toBe('Hello, world!');
        done();
      });
    });

    req.on('error', (e) => {
      done(e);
    });

    req.end();
  });
});
