import { mount } from '@vue/test-utils'
import WhiteBoard from '@/components/WhiteBoard'
describe('WhiteBoard', () => {
  it('has 4 divs', () =>{
    const wrapper = mount(WhiteBoard)
    const divs = wrapper.vm.findAll('div')
    expect(divs).toHaveLength(4)
  })
  it('has 7 buttons', () =>{
    const wrapper = mount(WhiteBoard)
    expect(wrapper.vm.findAll('el-button')).toHaveLength(7)
  })
  it('has 3 cards', () =>{
    const wrapper = mount(WhiteBoard)
    expect(wrapper.vm.findAll('el-card')).toHaveLength(3)
  })
})
