import { getMountWithVuex } from '../../../../jest/utils';
import ParticipantsChart from './ParticipantsChart';
import { getDateString, getYearBeforeDate } from '../../../helpers/date';

describe('ParticipantsChart component', () => {
  const mountWithVuex = getMountWithVuex();
  const todayDate = new Date();

  it('renders correctly', () => {
    const wrapper = mountWithVuex(ParticipantsChart);

    expect(wrapper).toBeDefined();
  });

  it('renders the title', () => {
    const wrapper = mountWithVuex(ParticipantsChart);

    expect(wrapper.get('[data-test-id=chart-title]').text()).toBe(
      'Participants on hacknights'
    );
    expect(wrapper.get('[data-test-id=chart-title]').isVisible()).toBe(true);
  });

  it('renders end date as today', done => {
    const wrapper = mountWithVuex(ParticipantsChart);

    wrapper.vm.$nextTick(() => {
      expect(wrapper.get('#end-date').element.value).toBe(
        getDateString(todayDate)
      );

      done();
    });
  });

  it('renders start day as year before today', done => {
    const wrapper = mountWithVuex(ParticipantsChart);

    wrapper.vm.$nextTick(() => {
      expect(wrapper.get('#start-date').element.value).toBe(
        getDateString(getYearBeforeDate(todayDate))
      );

      done();
    });
  });
});
