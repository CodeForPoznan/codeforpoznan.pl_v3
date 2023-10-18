import { shallowMount } from '@vue/test-utils';
import OurProjects from './OurProjects.vue';
import { expect, test, it } from 'vitest';

test('OurProjects component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(OurProjects);

    expect(wrapper).toBeDefined();
  });
});
