import { shallowMount } from '@vue/test-utils';
import DashboardHeader from './DashboardHeader.vue';
import { expect, test, it } from 'vitest';

test('DashboardHeader component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(DashboardHeader);

    expect(wrapper).toBeDefined();
  });
});
