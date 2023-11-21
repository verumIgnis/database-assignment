SELECT artistTable.artistSurname, artistTable.artistInitial,
CASE galleryTable.galleryTypeID WHEN 1 THEN '40%' ELSE '20%' END galleryTypeID,
CASE galleryTable.galleryTypeID WHEN 1 THEN 0.4 * exhibitionTable.predictedSales ELSE 0.2 * exhibitionTable.predictedSales END galleryTypeID
FROM exhibitionTable
JOIN artistTable ON exhibitionTable.artistID = artistTable.artistID
JOIN galleryTable ON exhibitionTable.galleryID = galleryTable.galleryID
JOIN galleryTypeTable ON galleryTable.galleryTypeID = galleryTypeTable.galleryTypeID;
WHERE artistSurname = ?