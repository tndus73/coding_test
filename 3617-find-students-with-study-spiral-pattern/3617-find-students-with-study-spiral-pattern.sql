# Write your MySQL query statement below
WITH ordered AS (
    SELECT
        ss.student_id,
        ss.subject,
        ss.session_date,
        ss.hours_studied,
        ROW_NUMBER() OVER ( -- 학생별 공부 기록에 순번을 매겨
            PARTITION BY ss.student_id
            ORDER BY ss.session_date, ss.session_id
        ) AS rn,
        DATEDIFF( -- 이전 공부일과 며칠 차이
            ss.session_date,
            LAG(ss.session_date) OVER (
                PARTITION BY ss.student_id
                ORDER BY ss.session_date, ss.session_id
            )
        ) AS gap_days
    FROM study_sessions ss
),

candidate AS ( -- 학생별 기본 요약
    SELECT
        student_id,
        COUNT(*) AS total_sessions, -- 총 몇 번 공부했는지
        COUNT(DISTINCT subject) AS cycle_length, -- 서로 다른 과목이 몇 개인지
        MAX(COALESCE(gap_days, 0)) AS max_gap, -- 날짜 간격 최대값
        SUM(hours_studied) AS total_study_hours -- 총 공부 시간
    FROM ordered
    GROUP BY student_id
),

pattern_check AS ( -- 반복 패턴인지 확인(앞 사이클과 뒤 사이클을 비교)
    SELECT
        o1.student_id,
        COUNT(*) AS matched_pairs -- 앞 vs 뒤 비교해서 같은 과목인 개수
    FROM ordered o1 -- 앞 사이클
    JOIN ordered o2 -- 뒤 사이클
      ON o1.student_id = o2.student_id
     AND o2.rn = o1.rn + (
         SELECT COUNT(DISTINCT subject) -- 앞 사이클과 뒤 사이클을 비교 o2.rn = o1.rn + cycle_length
         FROM ordered x
         WHERE x.student_id = o1.student_id
     )
    WHERE o1.rn <= ( -- 앞 사이클 부분만 보겠다
        SELECT COUNT(DISTINCT subject)
        FROM ordered x
        WHERE x.student_id = o1.student_id
    )
      AND o1.subject = o2.subject -- 같은 과목이 반복
    GROUP BY o1.student_id
)

SELECT
    s.student_id,
    s.student_name,
    s.major,
    c.cycle_length,
    c.total_study_hours
FROM candidate c
JOIN pattern_check p
  ON c.student_id = p.student_id
JOIN students s
  ON s.student_id = c.student_id
WHERE c.cycle_length >= 3 -- 서로 다른 과목이 최소 3개
  AND c.total_sessions >= c.cycle_length * 2 -- 적어도 2사이클
  AND c.max_gap <= 2 -- 연속 세션 간 간격이 2일 이하
  AND p.matched_pairs = c.cycle_length -- 앞 cycle과 뒤 cycle이 100% 동일한지 확인
ORDER BY c.cycle_length DESC, c.total_study_hours DESC;