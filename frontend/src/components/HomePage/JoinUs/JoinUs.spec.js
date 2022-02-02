import { shallowMount } from '@vue/test-utils';
import JoinUs from './JoinUs';

describe('JoinUs component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(JoinUs);

    expect(wrapper).toBeDefined();
  });
});
