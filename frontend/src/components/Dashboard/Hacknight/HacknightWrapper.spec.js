import HacknightWrapper from './HacknightWrapper.vue';
import { getMountWithProviders } from '../../../../jest/utils';
import { expect, test, it } from 'vitest';

test('HacknightWrapper component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(HacknightWrapper);

    expect(wrapper).toBeDefined();
  });
});
