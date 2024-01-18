-- Modified Script 1 to achieve the same result as Script 3
SELECT `cities`.`id`, `cities`.`name`
FROM `cities`
INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
WHERE `states`.`name` = 'California'
ORDER BY `cities`.`id`;
