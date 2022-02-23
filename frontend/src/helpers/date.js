export const getDateString = (dateObject, separator = '-') => {
  const mm = dateObject.getMonth() + 1; // getMonth() is zero-based
  const dd = dateObject.getDate();

  return [
    dateObject.getFullYear(),
    (mm > 9 ? '' : '0') + mm,
    (dd > 9 ? '' : '0') + dd
  ].join(separator);
};

export const getYearBeforeDate = todayDateObject => {
  const todayDateCopy = new Date(todayDateObject);

  todayDateCopy.setMonth(todayDateCopy.getMonth() - 12);

  return todayDateCopy;
};
