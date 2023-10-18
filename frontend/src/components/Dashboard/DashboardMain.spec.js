import DashboardMain from './DashboardMain.vue';
import { getMountWithProviders } from '../../../jest/utils';
import { expect, test, it } from 'vitest';

test('DashboardMain component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(DashboardMain);

    expect(wrapper).toBeDefined();
  });
});
