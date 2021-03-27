import { mount } from '@vue/test-utils'
import LessonList from '@/views/LessonList'
describe('LessonList', () => {
  const wrapper = mount(LessonList, {
    data() {
      return {
        value: new Date(),
        isTeacher: false,
        identity: 'student',
        studentId: "123",
        teacherId: "",
        studentName: "www",
        teacherName: "",
        lessonList: [{id:1,lessonId:"0001",lessonName:"大物",lessonNotice:"预习光的折射"},
        {id:2,lessonId:"0002",lessonName:"高数",lessonNotice:"本周三晚九十节答疑"}],
        lessonNotice: "",
        dialogVisible: false
      }
    }
  })
  it('has 6 divs', () => {
    const divs = wrapper.findAll('div')
    expect(divs).toHaveLength(14)
    expect(divs.at(0).element.id).toBe('LessonList')
    expect(divs.at(1).element.id).toBe('Header')
    expect(divs.at(2).element.id).toBe('Space')
    expect(divs.at(3).element.id).toBe('Exit')
    expect(divs.at(4).element.id).toBe('List')
    expect(divs.at(5).element.id).toBe('LessonRoom')
    expect(divs.at(6).element.id).toBe('LessonName')
    expect(divs.at(7).element.id).toBe('LessonNotice')
    expect(divs.at(8).element.id).toBe('Button1')
    expect(divs.at(9).element.id).toBe('LessonRoom')
    expect(divs.at(10).element.id).toBe('LessonName')
    expect(divs.at(11).element.id).toBe('LessonNotice')
    expect(divs.at(12).element.id).toBe('Button1')
    expect(divs.at(13).element.id).toBe('Calendar')
  }),
  it('Header has 2 divs', () => {
    const Header = wrapper.find('.Header')
    const headerDivs = Header.findAll('div')
    expect(headerDivs).toHaveLength(3)
    expect(headerDivs.at(0).element.id).toBe('Header')
    expect(headerDivs.at(1).element.id).toBe('Space')
    expect(headerDivs.at(2).element.id).toBe('Exit')
  }),
  it('text in Space and Exit', () => {
    const Space = wrapper.find('.Space')
    const Exit = wrapper.find('.Exit')
    expect(Space.text()).toBe('www 您本学期拥有的答疑课程如下:')
    expect(Exit.text()).toBe('返回')
  }),
  it('value of isTeacher', () => {
    expect(wrapper.vm.isTeacher).toBe(false)
    expect(wrapper.vm.identity).toBe('student')
  })
  it('lessonRoom exists', () => {
    const List = wrapper.find('.List')
    const ListDivs = List.findAll('div')
    expect(ListDivs).toHaveLength(9)
  })
  it('the first lessonroom', () => {
    const Rooms = wrapper.findAll('.LessonRoom')
    const Room_1 = Rooms.at(0)
    const name_1 = Room_1.find('.LessonName')
    expect(name_1.text()).toBe('大物')
  })
  it('the first lessonroom', () => {
    const Rooms = wrapper.findAll('.LessonRoom')
    const Room_2 = Rooms.at(1)
    const name_2 = Room_2.find('.LessonName')
    expect(name_2.text()).toBe('高数')
  })
})
