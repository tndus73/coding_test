WITH RECURSIVE levels AS (
    -- CEO부터 시작
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    -- 부하 직원으로 내려가며 level + 1 이미 levels에 들어간 직원 l이 있음 그 직원을 manager로 두는 직원 e를 찾음
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        l.level + 1
    FROM Employees e
    JOIN levels l
      ON e.manager_id = l.employee_id
),
closure AS ( -- 누구 밑에 누가 있는지 전부 펼치는 테이블이야.
    -- 자기 자신 포함(나중에 budget 계산할 때 본인 급여도 포함)
    SELECT
        employee_id AS ancestor, -- 상위 직원
        employee_id AS descendant -- 그 밑에 속한 직원
    FROM Employees

    UNION ALL

    -- descendant의 직접 부하를 계속 확장
    SELECT
        c.ancestor,
        e.employee_id AS descendant
    FROM closure c
    JOIN Employees e
      ON e.manager_id = c.descendant
      -- c.descendant가 누군가의 manager라면 e.employee_id도 결국 c.ancestor 밑에 있는 사람
),
agg AS (
    SELECT
        c.ancestor AS employee_id,
        COUNT(*) - 1 AS team_size, -- 자기 자신 제거
        SUM(e.salary) AS budget
    FROM closure c
    JOIN Employees e
      ON c.descendant = e.employee_id -- descendant(부하)의 id로 실제 직원 정보 가져오기”
    GROUP BY c.ancestor
)
SELECT
    l.employee_id,
    l.employee_name,
    l.level,
    a.team_size,
    a.budget
FROM levels l
JOIN agg a
  ON l.employee_id = a.employee_id
ORDER BY l.level, a.budget DESC, l.employee_name;