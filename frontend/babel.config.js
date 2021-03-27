module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  plugins: [
    [
      'component',
      {
        libraryName: 'jellies',
        libDir: 'src/components',
        styleLibraryName: 'theme'
      }
    ]
  ]
}
