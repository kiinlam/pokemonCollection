let request = require('request')
let fs = require('fs')

module.exports = function (url, pathname) {
  return new Promise((resolve, reject) => {
    request
      .get(url)
      .on('response', function (response) {
        console.log(`Downloaded image(${response.headers['content-type']}): ${url}`)
      })
      .pipe(fs.createWriteStream(pathname))
      .on('finish', function () {
        resolve(`Download image ${url} success`)
      })
      .on('error', function (error) {
        console.log(`Download image ${url} fail: ${error}`)
        resolve(`Download image ${url} fail: ${error}`)
      })
  })
}