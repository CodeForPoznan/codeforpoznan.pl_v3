import { shallowMount } from '@vue/test-utils';
import HomePageHeader from './HomePageHeader.vue';
import { expect, test, it } from 'vitest';

test('HomePageHeader component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(HomePageHeader);

    expect(wrapper).toBeDefined();
  });
});
