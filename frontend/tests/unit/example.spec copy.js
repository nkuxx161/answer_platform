function test (a) {
  if (a) {
    return 1;
  } else {
    return -1;
  }
}
describe('testA', () => {
  it('测试一', () => {
    test(false)
  })
})
