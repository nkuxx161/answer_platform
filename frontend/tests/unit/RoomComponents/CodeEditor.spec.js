import { mount } from '@vue/test-utils'
import CodeEditor from '@/components/CodeEditor'
describe('CodeEditor', () => {
  it('has 3 divs', () => {
    const wrapper = mount(CodeEditor)
    const divs = wrapper.findAll('div')
    expect(divs).toHaveLength(3)
  })
  it('has header', () => {
    const wrapper = mount(CodeEditor)
    expect(wrapper.find('el-header').exists()).toBe(true)
  })
  it('has two selects', () => {
    const wrapper = mount(CodeEditor)
    const selects = wrapper.findAll('el-select')
    expect(selects).toHaveLength(2)
  })
  it('has editor', () => {
    const wrapper = mount(CodeEditor)
    expect(wrapper.find('editor').exists()).toBe(true)
  })
})
