import { getMountWithProviders } from '../../../../jest/utils';
import ParticipantsList from './ParticipantsList';

describe('ParticipantsList component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(ParticipantsList);

    expect(wrapper).toBeDefined();
  });
});
