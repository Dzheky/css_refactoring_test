// import purgecss from '@fullhuman/postcss-purgecss'
import modules from 'postcss-modules'

export default (ctx) => ({
  plugins: [
    // purgecss({
    //   content: ['./**/*.html']
    // })
    modules({
      generateScopedName: '[name]__[local]___[hash:base64:5]'
    })
  ]
})