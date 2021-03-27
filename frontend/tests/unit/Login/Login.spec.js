import {mount} from '@vue/test-utils'
import Login from '@/views/Login'

describe('Login.vue', () => {
  it('correct contents', () => {
    const wrapper = mount(Login)
    const h1 = wrapper.find('h1')
    expect(h1.text())
    .toBe('登录')
  })
  it('button number', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('el-button')).toBe(true)
  })
  it('renders a div', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('div')).toBe(true)
  })
  it('input exsit', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('input')).toBe(true)
  })
  it('span exsit', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('span')).toBe(true)
  })
  it('choose student', () => {
    const wrapper = mount(Login)
    wrapper.vm.studentLogin()
    expect(wrapper.vm.identity).toBe('student')
  })
  it('choose teacher', () => {
    const wrapper = mount(Login)
    wrapper.vm.teacherLogin()
    expect(wrapper.vm.identity).toBe('teacher')
  })
  it('choose admin', () => {
    const wrapper = mount(Login)
    wrapper.vm.adminLogin()
    expect(wrapper.vm.identity).toBe('admin')
  })
  it('login student', () => {
    const wrapper = mount(Login)
    wrapper.find('.student input').trigger('click')
    wrapper.vm.loginName = "333@qq.com"
    wrapper.vm.password = "333"
    wrapper.find('.login').trigger('click')
    expect(wrapper.vm.loginName).toBe('333@qq.com')
    expect(wrapper.vm.password).toBe('333')
  })
  it('login teacher', () => {
    const wrapper = mount(Login)
    wrapper.find('.teacher input').trigger('click')
    wrapper.vm.loginName = "444@qq.com"
    wrapper.vm.password = "444"
    wrapper.find('.login').trigger('click')
    expect(wrapper.vm.loginName).toBe('444@qq.com')
    expect(wrapper.vm.password).toBe('444')
  })
})
