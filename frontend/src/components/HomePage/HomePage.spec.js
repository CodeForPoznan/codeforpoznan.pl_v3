import { getMountWithProviders } from '../../../jest/utils';
import HomePage from './HomePage.vue';
import { expect, test, it } from 'vitest';

test('HomePage component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HomePage);

    expect(wrapper).toBeDefined();
  });
});
