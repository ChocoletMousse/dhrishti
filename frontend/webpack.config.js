const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { template } = require('@babel/core');

module.exports = {
    entry: './src/index.js',
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
        path: path.join(__dirname, 'dist')
    },
    devServer: {
        contentBase: path.join(__dirname, 'public'),
        compress: true,
        port: 8000
    },
    watch: false,
    plugins: [
        new HtmlWebpackPlugin({
            template: path.join(__dirname, 'public/index.html'),
            filename: 'index.html'
        })
    ]
}