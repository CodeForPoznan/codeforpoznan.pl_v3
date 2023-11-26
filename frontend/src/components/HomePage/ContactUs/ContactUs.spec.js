import { shallowMount } from '@vue/test-utils';
import ContactUs from './ContactUs.vue';
import { expect, test, it } from 'vitest';

test('ContactUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(ContactUs);

    expect(wrapper).toBeDefined();
  });
});
