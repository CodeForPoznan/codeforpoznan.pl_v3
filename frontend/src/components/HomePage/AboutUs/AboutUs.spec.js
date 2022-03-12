import { shallowMount } from '@vue/test-utils';
import AboutUs from './AboutUs';

describe('AboutUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(AboutUs);

    expect(wrapper).toBeDefined();
  });
});
