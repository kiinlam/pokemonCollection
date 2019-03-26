const path = require('path')
const URL = require('url')
const makeDir = require('make-dir')
const downloadImage = require('./downloadImage')
const datalist = require('../database/all.json')
const baseUrl = 'https://cn.portal-pokemon.com/play/resources/pokedex'

function getPath(url) {
  let pathname = URL.parse(url).pathname
  pathname = path.join('./', pathname)
  pathname = path.resolve(pathname)
  return pathname
}

async function download(datalist) {
  for (let item of datalist) {
    let url = baseUrl + item.file_name
    let pathname = getPath(item.file_name)
    await makeDir(path.dirname(pathname))
    await downloadImage(url, pathname)
  }
}

download(datalist)
