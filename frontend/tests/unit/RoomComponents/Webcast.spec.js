import { mount } from '@vue/test-utils'
import Webcast from '@/components/Webcast'
describe('Webcast', () => {
  it('has 3 divs', () => {
    const wrapper = mount(Webcast)
    const divs = wrapper.findAll('div')
    expect(divs).toHaveLength(3)
  })
  it('has videoPlayer', () => {
    const wrapper = mount(Webcast)
    expect(wrapper.find('video-player').exists()).toBe(true)
  })
  it('has 3 buttons', () => {
    const wrapper = mount(Webcast)
    const buttons = wrapper.findAll('el-button')
    expect(buttons).toHaveLength(3)
  })
})
