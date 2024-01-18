-- Ld
SELECT `id`, `name`
  FROM `cities`
 INNER JOIN `states` ON `cities`.`state_id` == `states`.`id`
 ORDER BY `id`;
