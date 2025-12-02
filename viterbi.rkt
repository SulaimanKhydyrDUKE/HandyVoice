(define (deep-reverse x)
  (cond [(null? x) '()]
        [(pair? (car x))(append (deep-reverse (cdr x))(list (deep-reverse (car x))))]
        [else(append (deep-reverse (cdr x))(list (car x)))]) )


(deep-reverse '())
()
(reverse '(1 (2 3) 4 5))
(deep-reverse '(1 (2 3) 4 5))
(reverse '(1 (2 3) (4 (5 6) 7) (8 9 (10 11 (12)))))
(deep-reverse '(1 (2 3) (4 (5 6) 7) (8 9 (10 11 (12)))))


(define viterbiProb
  (emission k switchPr p1 p2)
  (cond[(null? (cdr emission))
        1]
       [(
         (let ((most_likely (car ((loop (cdr emission) (- k 1) switchPr p1 p2))))
               (second_likely (car (cdr ((loop (cdr emission) (- k 1) switchPr p1 p2)))))
               (is_ml_p1 (if ( = (car most_likely) p1) #t #f)))
         (cons 
               ( (if (is_ml_p1)
                     (pair p1 (max( (* (loop (cdr emission) (- k 1) switchPr p1 p2) switchPr (car (second_likely)))
                                    (* (loop (cdr emission) (- k 1) switchPr p1 p2) (- 1 switchPr) (car (most_likely))))))
                     
                     (pair p1 (max( (* (loop (cdr emission) (- k 1) switchPr p1 p2) (- 1 switchPr) (car (second_likely)))
                                    (* (loop (cdr emission) (- k 1) switchPr p1 p2) switchPr (car (most_likely))))))
                     )
                 ;;Where do I pass on the inverse probabilites? FUUUU
               (pair (p2 ( max(* ())
                             (* () ) ) )))))]
;Max of (Viterbi(k-1, p1)*switchPr*p1,
   ;     Vitervi(k-1, p2)*(1-switchPr)*p1)
   ))  
