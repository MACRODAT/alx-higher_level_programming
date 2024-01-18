-- Ld
SELECT `id`, `name`
  FROM `cities`
 INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
 WHERE `states`.`name` = 'California'
 ORDER BY `id`;
