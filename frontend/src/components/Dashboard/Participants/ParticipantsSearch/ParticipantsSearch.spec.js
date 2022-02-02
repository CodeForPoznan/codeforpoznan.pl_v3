import { getMountWithProviders } from '../../../../../jest/utils';
import ParticipantsSearch from './ParticipantsSearch';

describe('ParticipantsSearch component', () => {
  const mountWithProviders = getMountWithProviders();

  it('renders correctly', () => {
    const wrapper = mountWithProviders(ParticipantsSearch);

    expect(wrapper).toBeDefined();
  });
});
