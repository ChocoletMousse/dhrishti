const path = require('path');

module.exports = {
    entry: './frontend/src/index.js',
    module: {
        rules: [
            { 
                test: /\.js$/, 
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    },
    output:  {
        filename: 'bundle.js',
        path: path.join(__dirname, 'frontend/static/frontend')
    },
    watch: false
}