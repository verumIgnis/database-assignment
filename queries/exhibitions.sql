SELECT galleryTable.galleryName, galleryTypeTable.galleryType, exhibitionTable.numDays, exhibitionTable.startDate, exhibitionTable.startDate
FROM exhibitionTable
JOIN galleryTable ON exhibitionTable.galleryID = galleryTable.galleryID
JOIN galleryTypeTable ON galleryTable.galleryTypeID = galleryTypeTable.galleryTypeID
WHERE exhibitionTable.numDays >= 5 AND galleryTypeTable.galleryType = 'Commercial'
ORDER BY galleryTable.galleryName;