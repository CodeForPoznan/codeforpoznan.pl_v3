import { shallowMount } from '@vue/test-utils';
import JoinUs from './JoinUs.vue';
import { expect, test, it } from 'vitest';

test('JoinUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(JoinUs);

    expect(wrapper).toBeDefined();
  });
});
