import { shallowMount } from '@vue/test-utils';
import AboutUs from './AboutUs.vue';
import { expect, test, it } from 'vitest';

test('AboutUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(AboutUs);

    expect(wrapper).toBeDefined();
  });
});
