import { shallowMount } from '@vue/test-utils';
import Header from './Header';

describe('Header component', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(Header);

    expect(wrapper).toBeDefined();
  });
});
