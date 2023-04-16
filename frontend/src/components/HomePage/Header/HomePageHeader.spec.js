import { shallowMount } from '@vue/test-utils';
import HomePageHeader from './HomePageHeader';

describe('HomePageHeader component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(HomePageHeader);

    expect(wrapper).toBeDefined();
  });
});
