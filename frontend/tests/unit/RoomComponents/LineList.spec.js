import {mount} from '@vue/test-utils'
import LineList from '@/components/LineList'

describe('LineList', () => {
  it('has 4 divs', () => {
    const wrapper = mount(LineList)
    const divs = wrapper.findAll('div')
    expect(divs).toHaveLength(4)
  })
  it('has 2 buttons', () => {
    const wrapper = mount(LineList)
    const buttons = wrapper.findAll('el-button')
    expect(buttons).toHaveLength(2)
  })
  it('could inline', () => {
    const wrapper = mount(LineList)
    wrapper.vm.studentName = "Jack"
    wrapper.vm.studentId = "123"
    wrapper.vm.lessonId = "0001"
    wrapper.findAll('el-button').at(0).trigger('click')
    expect(wrapper.vm.studentName).toBe("Jack")
  })
  it('could outline', () => {
    const wrapper = mount(LineList)
    wrapper.vm.studentName = "Jack"
    wrapper.vm.studentId = "123"
    wrapper.vm.lessonId = "0001"
    wrapper.findAll('el-button').at(1).trigger('click')
    const ol = wrapper.find('ol')
    const lis = ol.findAll('li')
    expect(lis).toHaveLength(0)
  })
})
