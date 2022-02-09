import { shallowMount } from '@vue/test-utils';
import DashboardHeader from './DashboardHeader';

describe('DashboardHeader component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(DashboardHeader);

    expect(wrapper).toBeDefined();
  });
});
