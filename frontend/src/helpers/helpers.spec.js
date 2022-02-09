import { getDateString } from './date.js';

describe('getDateString util', () => {
  const date = new Date('December 17, 1995 03:24:00');

  it('should convert date object to string', () => {
    expect(getDateString(date)).toEqual('1995-12-17');
  });

  it('should convert date object to string with passed separator', () => {
    expect(getDateString(date, '/')).toEqual('1995/12/17');
  });
});
