import DashboardMain from './DashboardMain';
import { getMountWithProviders } from '../../../jest/utils';

describe('DashboardMain component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(DashboardMain);

    expect(wrapper).toBeDefined();
  });
});
