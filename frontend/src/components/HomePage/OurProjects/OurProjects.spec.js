import { shallowMount } from '@vue/test-utils';
import OurProjects from './OurProjects';

describe('OurProjects component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(OurProjects);

    expect(wrapper).toBeDefined();
  });
});
