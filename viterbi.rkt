(define (viterbiPath emission switchPr s1 s2 p1 p2)
  (letrec
      ([step
        (lambda (EM prev)
          ;; prev = ((s1 prob1 path1) (s2 prob2 path2))
          (let* ((x (car EM))
                 (is_inverse (= x 1))
                 (emit1 (if is_inverse (- 1 p1) p1))
                 (emit2 (if is_inverse (- 1 p2) p2)))

            (let* ((prev1 (car prev))
                   ; (s1 prob path)
                   (prev2 (cadr prev))
                   (p1_prev (cadr prev1))
                   (p2_prev (cadr prev2))
                   (path1_prev (caddr prev1))
                   (path2_prev (caddr prev2))
                   (stay1 (* p1_prev (- 1 switchPr)))
                   (switch2 (* p2_prev switchPr))
                   (stay2 (* p2_prev (- 1 switchPr)))
                   (switch1 (* p1_prev switchPr))
                   
                   (new1_raw-stay (* stay1 emit1))
                   (new1_raw-switch (* switch2 emit1))
                   (new2_raw-stay (* stay2 emit2))
                   (new2_raw-switch (* switch1 emit2))
                   (new1 (if (> new1_raw-stay new1_raw-switch)
                             (list s1 new1_raw-stay (append path1_prev (list s1)
                                                            )
                                   )
                             (list s1 new1_raw-switch (append path2_prev (list s1)))
                             ))

                   (new2 (if (> new2_raw-stay new2_raw-switch)
                             (list s2 new2_raw-stay (append path2_prev (list s2)))
                             (list s2 new2_raw-switch (append path1_prev (list s2))))))

              (list new1 new2))))]

       ;; BASE CASE
       [init
        (let ((x (car emission)))
          (let ((is_inverse (= x 1)))
            (list
             (list s1 (* 0.5 (if is_inverse (- 1 p1) p1)) (list s1))
             (list s2 (* 0.5 (if is_inverse (- 1 p2) p2)) (list s2)))))])

    ;; RC
    (let loop ((EM (cdr emission))
               (prev init))
      (if (null? EM)
          ;; choose best final one
          (let* ((p1-prev (cadr (car prev)))
                 (p2-prev (cadr (cadr prev))))
            (if (> p1-prev p2-prev)
                (list (caddr (car prev)) p1-prev)
                (list (caddr (cadr prev)) p2-prev)))
          (loop (cdr EM) (step EM prev))))))
